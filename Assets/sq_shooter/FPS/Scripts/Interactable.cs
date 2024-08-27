using UnityEngine;

public class Trigger : MonoBehaviour
{
    [SerializeField] private bool triggerActive = false;

    
    private void Update()
    {
        void OnTriggerEnter(Collider Cube)
        {
            if (Cube.CompareTag("Player"))
            {
                triggerActive = true;
            }
        }

        void OnTriggerExit(Collider Cube)
        {
            if (Cube.CompareTag("Player"))
            {
                triggerActive = false;
            }
        }

        if (triggerActive && Input.GetKeyDown(KeyCode.F))
        {
            SomeCoolAction();
        }
    }

    public void SomeCoolAction()
    {
        Debug.Log("Trigger active");
    }
}