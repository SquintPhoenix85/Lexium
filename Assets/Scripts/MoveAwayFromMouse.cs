using UnityEngine;

public class RepelFromMouse : MonoBehaviour
{
    public float repelForce = 5f; // Fuerza de repulsión
    private Rigidbody2D rb;

    void Start()
    {
        // Obtener el componente Rigidbody2D
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        RepelFromMousePosition();
    }

    void RepelFromMousePosition()
    {
        // Obtener la posición del mouse en el mundo
        Vector3 mousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        mousePosition.z = 0; // Asegurarse de que el z sea 0 para 2D

        // Calcular la dirección desde el mouse hacia el objeto
        Vector2 repelDirection = (Vector2)(transform.position - mousePosition).normalized;

        // Aplicar fuerza en la dirección contraria al mouse
        rb.AddForce(repelDirection * repelForce);
    }
}
