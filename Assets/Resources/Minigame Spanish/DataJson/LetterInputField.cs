using UnityEngine;
using UnityEngine.UI;

public class LetterInputField : MonoBehaviour
{
    public InputField inputField;
    public Text outputText;
    public LetterAssociation letterAssociation;

    void Start()
    {
        inputField.onValueChanged.AddListener(OnInputValueChanged);
    }

    void OnInputValueChanged(string input)
    {
        char inputLetter = input[0]; // assume only one character is entered
        char associatedLetter = letterAssociation.GetAssociatedLetter(inputLetter);
        outputText.text = associatedLetter.ToString();
    }
}