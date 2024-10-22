using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

[System.Serializable]
public class PalabrasData
{
    public List<string> palabras;
}

public class WordChanger : MonoBehaviour
{
    public Text texto;
    public Button boton;
    public TextAsset jsonFile;
    private PalabrasData palabrasData;
    private int indexActual = 0;

    // Start is called before the first frame update
    void Start()
    {
        if(jsonFile != null)
        {
            palabrasData = JsonUtility.FromJson<PalabrasData>(jsonFile.text);
        }
        else
        {
            Debug.LogError("No se ha asignado el archivo JSON en el inspector.");
        }
        NextWord();
    }

    // Update is called once per frame
    public void NextWord()
    {
        if (palabrasData != null && palabrasData. palabras.Count > 0 )
        {
            texto.text = palabrasData.palabras[indexActual];
            indexActual = (indexActual + 1)% palabrasData.palabras.Count;
        }
    }
}
