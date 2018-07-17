using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityStandardAssets.Characters.ThirdPerson;

public class prizepickup : MonoBehaviour {

	public HUD_Manager HUD_Manager;
	public ThirdPersonCharacter ThirdPersonCharacter;
	public int points; 
	
	public float JunpIncrease; 
	public float SpeedIncrease;

	void Start() { 
	    HUD_Manager = GameObject.FindGameObjectWithTag ("Player").GetComponent<HUD_Manager> ();
		ThirdPersonCharacter = GameObject.Find ("Player").GetComponent<ThirdPersonCharacter> ();
	}

	void OnTriggerEnter(Collider other){
  		if (other.gameObject.CompareTag ("Player")) {
	 		gameObject.SetActive (false);
		 	HUD_Manager.UpdateScore(points);
			} 	
	}
}