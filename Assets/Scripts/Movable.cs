using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movable : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    private float _pushPower = 2f;

    private void OnControllerColliderHit(ControllerColliderHit hit)
    {
        if (hit.transform.tag == "Movable")
        {
            Rigidbody Mug = hit.collider.GetComponent<Rigidbody>();

            if (Mug != null)
            {
                Vector3 pushDirection = new Vector3(hit.moveDirection.x, 0, 0);
                Mug.velocity = pushDirection * _pushPower;
            }
        }

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
