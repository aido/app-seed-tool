from pytest import mark
from pytest import skip
from ledgered.devices import Device, DeviceType
from ragger.firmware.touch.positions import POSITIONS
from ragger.navigator import Navigator, NavIns, NavInsID
from genericlayout import GenericLayout  # noqa: F401  (registers its positions)

# Centre of the back button that generic_screen_set_back_button() draws in
# src/nbgl/layout_generic_screen.c: a BUTTON_DIAMETER square, aligned TOP_LEFT,
# 4 pixels down. BUTTON_DIAMETER is COMMON_RADIUS * 2, so 80 on Stax, 88 on
# Flex and 56 on Apex.
BACK_BUTTON = {
    DeviceType.STAX: (40, 44),
    DeviceType.FLEX: (44, 48),
    DeviceType.APEX_P: (28, 32),
}


def _back(device: Device) -> NavIns:
    return NavIns(NavInsID.TOUCH, BACK_BUTTON[device.type])


def _choice(device: Device, index: int) -> NavIns:
    # 1 is the bottom-most button, as in the other functional tests.
    position = POSITIONS["GenericLayout"][device.type][index]
    return NavIns(NavInsID.TOUCH, (position.x, position.y))


def _home_action(device: Device) -> NavIns:
    position = POSITIONS["UseCaseHomeExt"][device.type]["action"]
    return NavIns(NavInsID.TOUCH, (position.x, position.y))


# The other functional tests drive the application through its entry flows and
# assert on text read back from the screen, which cannot see a purely visual
# regression: a moved label, a swapped icon, an extra page. This one compares
# full screenshots instead, over the screens that do not depend on any input.
#
# Deliberately out of scope: everything behind the keyboard and the keypad. A
# 24-word entry is several hundred screens per device, and any ergonomic touch
# -- one more suggestion button, a different page break -- would invalidate all
# of them at once.
@mark.use_on_backend("speculos")
def test_app_mainmenu(device: Device, navigator: Navigator, test_name: str,
                      default_screenshot_path: str) -> None:
    if device.is_nano:
        # The BAGL screens are laid out by src/bagl/ and have their own
        # navigation; covering them is a separate piece of work.
        skip(f"Skipping test for {device.name} device")

    instructions = [
        # Home -> the information page, which carries the version
        NavInsID.USE_CASE_HOME_SETTINGS,
        # ... and back
        NavInsID.USE_CASE_SETTINGS_SINGLE_PAGE_EXIT,
        # Home -> "Select the tool you wish to use"
        _home_action(device),
        # -> "How long is your BIP39 Recovery Phrase?"
        _choice(device, 1),
        _back(device),
        # -> "Which BIP85 application?"
        _choice(device, 3),
        _back(device),
        # -> home
        _back(device),
    ]

    navigator.navigate_and_compare(
        default_screenshot_path,
        test_name,
        instructions,
        screen_change_before_first_instruction=False,
    )
