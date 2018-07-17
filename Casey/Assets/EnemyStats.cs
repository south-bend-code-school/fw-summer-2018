using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyStats : MonoBehaviour {

	public int startingHealth; 
	public int currentHealth;
    public Transform gold;

	public void Death (){
		  gameObject.SetActive (false);
		  Instantiate(gold, transform.position, Quaternion.identity);


	}
	// Use this for initialization
	public void Start () {
		currentHealth = startingHealth;
	}
	
	// Update is called once per frame
	public void UpdateHealth (int amount) {
			currentHealth = currentHealth - amount;
			if (currentHealth <= 0){
				Death();
			}
		
	}
}
