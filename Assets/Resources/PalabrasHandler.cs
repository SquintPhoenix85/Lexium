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
    TextAsset archivoJSON = Resources.Load<TextAsset>("Assets/Resources/ListaPalabras");
        if (archivoJSON != null)
        {
            JsonData data = JsonUtility.FromJson<JsonData>(archivoJSON.text);
            Debug.Log("Loaded JSON file: " + archivoJSON);
            palabras = data.ListaPalabras;
        }
        else
        {
            Debug.Log("Error - No se pudo cargar Lista Palabras");
            return;
        }
    }

    public void CambiarTexto()
    {
        if (palabrasMostrar == null)
        {
            Debug.LogError("palabrasMostrar is null!");
            return;
        }

        if (palabras == null)
        {
            Debug.LogError("palabras is null!");
            return;
        }

        if (palabras.Count == 0)
        {
            Debug.LogError("palabras is empty!");
            return;
        }

        currentIndex = (currentIndex+1)%palabras.Count;
        palabrasMostrar.text = palabras[currentIndex];
    }
}
