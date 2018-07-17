using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerHit : MonoBehaviour {

	public int AttackDamage;
	public HUD_Manager HUD_Manager;

	void Start () {
		HUD_Manager = GameObject.FindGameObjectWithTag ("Player").GetComponent<HUD_Manager> ();

		
		
	}
	private void OnTriggerEnter(Collider other) {
		if (other.gameObject.CompareTag ("Player")){
			HUD_Manager.UpdateHealth (AttackDamage);
	}
	}
}
