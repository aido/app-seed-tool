from pytest import fixture
from pytest import mark
from ragger.navigator import NavInsID
from ragger.conftest import configuration

@fixture(scope='session')
def set_seed():
    configuration.OPTIONAL.CUSTOM_SEED = "profit result tip galaxy hawk immune hockey series melody grape unusual prize nothing federal dad crew pact sad"

def nanos_bip39_18word(backend, navigator):
    backend.wait_for_text_on_screen("Check BIP39", 5)
    backend.wait_for_text_on_screen("recovery phras", 1)
    instructions = [
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.RIGHT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.LEFT_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK,
        NavInsID.BOTH_CLICK
    ]
    navigator.navigate(instructions, screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("BIP39 Phrase", 5)
    backend.wait_for_text_on_screen("is correct", 1)
    navigator.navigate([NavInsID.RIGHT_CLICK], screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("Quit", 1)
    navigator.navigate([NavInsID.RIGHT_CLICK], screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("Generate", 1)
    backend.wait_for_text_on_screen("SSKR phrases", 1)
    navigator.navigate([NavInsID.BOTH_CLICK], screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("Select number", 1)
    backend.wait_for_text_on_screen("of shares", 1)
    navigator.navigate([NavInsID.RIGHT_CLICK,
                        NavInsID.RIGHT_CLICK,
                        NavInsID.RIGHT_CLICK,
                        NavInsID.BOTH_CLICK],
                        screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("Select", 1)
    backend.wait_for_text_on_screen("threshold", 1)
    navigator.navigate([NavInsID.RIGHT_CLICK,
                        NavInsID.RIGHT_CLICK,
                        NavInsID.BOTH_CLICK],
                        screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("SSKR Share #1", 5)
    backend.wait_for_text_on_screen("tuna next keep hard", 1)
    navigator.navigate_until_text(NavInsID.RIGHT_CLICK, [], "SSKR Share #2", 20, screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("tuna next keep hard", 1)
    navigator.navigate_until_text(NavInsID.RIGHT_CLICK, [], "SSKR Share #3", 20, screen_change_before_first_instruction=False)
    backend.wait_for_text_on_screen("tuna next keep hard", 1)
    navigator.navigate_until_text(NavInsID.RIGHT_CLICK, [], "Quit", 20, screen_change_before_first_instruction=False)

def stax_bip39_18word(backend):
    backend.wait_for_text_on_screen("Seed Tool", 10)
    backend.finger_touch(106, 510, 1)
    backend.wait_for_text_on_screen("BIP39 Check", 5)
    backend.finger_touch(124, 601, 1)
    backend.finger_touch(200, 520, 1)
    backend.wait_for_text_on_screen("Enter word", 5)
    backend.finger_touch(380, 464, 1) # p
    backend.finger_touch(140, 464, 1) # r
    backend.finger_touch(340, 464, 1) # o
    backend.finger_touch(160, 520, 1) # f
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(140, 464, 1) # r
    backend.finger_touch(100, 464, 1) # e
    backend.finger_touch(80, 520, 1) # s
    backend.finger_touch(260, 464, 1) # u
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(180, 464, 1) # t
    backend.finger_touch(300, 464, 1) # i
    backend.finger_touch(380, 464, 1) # p
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(200, 520, 1) # g
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(360, 520, 1) # l
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(240, 520, 1) # h
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(60, 464, 1) # w
    backend.finger_touch(320, 520, 1) # k
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(300, 464, 1) # i
    backend.finger_touch(260, 576, 1) # m
    backend.finger_touch(260, 576, 1) # m
    backend.finger_touch(260, 464, 1) # u
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(240, 520, 1) # h
    backend.finger_touch(340, 464, 1) # o
    backend.finger_touch(100, 576, 1) # c
    backend.finger_touch(320, 520, 1) # k
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(80, 520, 1) # s
    backend.finger_touch(100, 464, 1) # e
    backend.finger_touch(140, 464, 1) # r
    backend.finger_touch(300, 464, 1) # i
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(260, 576, 1) # m
    backend.finger_touch(100, 464, 1) # e
    backend.finger_touch(360, 520, 1) # l
    backend.finger_touch(340, 464, 1) # o
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(200, 520, 1) # g
    backend.finger_touch(140, 464, 1) # r
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(380, 464, 1) # p
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(260, 464, 1) # u
    backend.finger_touch(220, 576, 1) # n
    backend.finger_touch(260, 464, 1) # u
    backend.finger_touch(80, 520, 1) # s
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(380, 464, 1) # p
    backend.finger_touch(140, 464, 1) # r
    backend.finger_touch(300, 464, 1) # i
    backend.finger_touch(20, 576, 1) # z
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(220, 576, 1) # n
    backend.finger_touch(340, 464, 1) # o
    backend.finger_touch(180, 464, 1) # t
    backend.finger_touch(240, 520, 1) # h
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(160, 520, 1) # f
    backend.finger_touch(100, 464, 1) # e
    backend.finger_touch(120, 520, 1) # d
    backend.finger_touch(100, 464, 1) # e
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(120, 520, 1) # d
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(120, 520, 1) # d
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(100, 576, 1) # c
    backend.finger_touch(140, 464, 1) # r
    backend.finger_touch(100, 464, 1) # e
    backend.finger_touch(60, 464, 1) # w
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(380, 464, 1) # p
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(100, 576, 1) # c
    backend.finger_touch(180, 464, 1) # t
    backend.finger_touch(100, 280, 1)
    backend.finger_touch(80, 520, 1) # s
    backend.finger_touch(40, 520, 1) # a
    backend.finger_touch(120, 520, 1) # d
    backend.finger_touch(100, 280, 1)
    backend.wait_for_text_on_screen("Correct Secret", 5)
    backend.wait_for_text_on_screen("Recovery Phrase", 1)
    backend.finger_touch(200, 630, 1)
    backend.wait_for_text_on_screen("Generate SSKR", 5)
    backend.finger_touch(200, 550, 1)
    backend.wait_for_text_on_screen("Enter number of SSKR shares", 5)
    backend.finger_touch(340, 300, 1) # 3
    backend.finger_touch(340, 600, 1)
    backend.wait_for_text_on_screen("Enter threshold value", 5)
    backend.finger_touch(195, 300, 1) # 2
    backend.finger_touch(340, 600, 1)
    backend.wait_for_text_on_screen("SSKR Share", 5)
    backend.wait_for_text_on_screen("tuna next keep hard", 1)
    backend.wait_for_text_on_screen("1 of 3", 1)
    backend.finger_touch(360, 630, 1)
    backend.wait_for_text_on_screen("SSKR Share", 5)
    backend.wait_for_text_on_screen("tuna next keep hard", 1)
    backend.wait_for_text_on_screen("2 of 3", 1)
    backend.finger_touch(360, 630, 1)
    backend.wait_for_text_on_screen("SSKR Share", 5)
    backend.wait_for_text_on_screen("tuna next keep hard", 1)
    backend.wait_for_text_on_screen("3 of 3", 1)
    backend.finger_touch(80, 630, 1)
    backend.wait_for_text_on_screen("Seed Tool", 5)
    backend.finger_touch(200, 630, 1)

@mark.use_on_backend("speculos")
def test_bip39_18word(firmware, backend, navigator, set_seed):
    if firmware.device == "nanos":
        nanos_bip39_18word(backend, navigator)
    elif firmware.device == "stax":
        stax_bip39_18word(backend)

