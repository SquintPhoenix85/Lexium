using System;
using System.Collections.Generic;
using UnityEngine;

public class LetterAssociation : MonoBehaviour
{
    // Constante para la lista de letras del alfabeto inglés
    private const string ALFABETO_INGLES = "abcdefghijklmnopqrstuvwxyz";

    // Dictionary to store the letter associations
    private Dictionary<char, char> letterAssociations = new Dictionary<char, char>();

    // List of all possible letters
    private List<char> allLetters = new List<char>(ALFABETO_INGLES);

    void Start()
    {
        // Initialize the letter associations
        InitializeLetterAssociations();
    }

    // Function to initialize the letter associations
    private void InitializeLetterAssociations()
    {
        // Clear the dictionary
        letterAssociations.Clear();

        // Shuffle the list of all letters
        Shuffle(allLetters);

        // Create the letter associations
        for (int i = 0; i < allLetters.Count; i++)
        {
            char currentLetter = allLetters[i];
            char associatedLetter = allLetters[(i + 1) % allLetters.Count]; // wrap around to the start of the list if we reach the end
            letterAssociations.Add(currentLetter, associatedLetter);
        }
    }

    // Function to shuffle a list
    private void Shuffle<T>(List<T> lista)
    {
        System.Random random = new System.Random();
        int n = lista.Count;
        while (n > 1)
        {
            n--;
            int k = random.Next(n + 1);
            T valor = lista[k];
            lista[k] = lista[n];
            lista[n] = valor;
        }
    }

    // Function to get the associated letter for a given letter
    public char GetAssociatedLetter(char inputLetter)
    {
        if (char.IsLetter(inputLetter) && letterAssociations.TryGetValue(inputLetter, out char associatedLetter))
        {
            return associatedLetter;
        }
        else
        {
            return inputLetter; // return the original letter if no association is found
        }
    }
}
