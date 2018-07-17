using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DamageEnemy : MonoBehaviour {
public int  attackDamage;
	
      void OnTriggerEnter(Collider other) {
		  	EnemyStats EnemyStats = other.GetComponent<EnemyStats>();

		if(EnemyStats != null){
			EnemyStats.UpdateHealth(attackDamage); 

	}
	
	
		
	}
}
