using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PalabrasHandler : MonoBehaviour
{
    public Text palabrasMostrar;
    public Button palabrasMostrarButton;
    private List < string > palabras;
    private int currentIndex = 0;

    [System.Serializable]
    public class JsonData
    {
        public List<string> ListaPalabras;
    }
    void Start()
    {
        TextAsset archivoJSON = Resources.Load<TextAsset>("ListaPalabras.json");
        if (archivoJSON != null)
        {
            JsonData data = JsonUtility.FromJson<JsonData>(archivoJSON.text);
            palabras = data.ListaPalabras;
        }
        else
        {
            Debug.Log("Error - No se pudo cargar Lista Palabras");
        }
    }

    public void CambiarTexto()
    {
        currentIndex = (currentIndex+1)%palabras.Count;
        palabrasMostrar.text = palabras[currentIndex];
    }
}
