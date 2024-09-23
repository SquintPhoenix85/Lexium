using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelLoader : MonoBehaviour
{
    // Declare 'e' as a class-level variable
    public bool e = false;

    public Animator transition;

    // Update is called once per frame
    public void Update()
    {
        if (Input.GetKeyDown(KeyCode.E))
        {
            e = true;
        }
    }

    public void OnTriggerEnter(Collider other)
    {
        if (other.tag == "LevelExit" && e == true)
        {
            StartCoroutine(LoadLevel(2));
        }
        else if (other.tag == "LevelStart")
        {
            StartCoroutine(LoadLevel(SceneManager.GetActiveScene().buildIndex + 1));
        }
    }
    IEnumerator LoadLevel(int levelIndex)
    {
        transition.SetTrigger("Start");
        yield return new WaitForSeconds(1);
        SceneManager.LoadScene(levelIndex);
    }
}