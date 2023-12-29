from plates import isValid

def test_isValid():
    assert isValid("AAA222") == True
    assert isValid("222AAA") == False
    assert isValid("A") == False
    assert isValid("AA222!") == False
    assert isValid("Bobby4") == True
    assert isValid("ISeeU2") == True
    #asserts values and checks the output
    
#Note to self - use -s for this test and any other test that uses break