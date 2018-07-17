using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class HUD_Manager : MonoBehaviour {

	
 public int MasterScore; 
 public Text ScoreText; 
public Slider PlayerHealthBar;
public int StartingHealth;
public int CurrentHealth;  

    void Start() {
	    MasterScore = 0;
        ScoreText = GameObject.Find ("ScoreText").GetComponent<Text> ();
		ScoreText.text = "Score: " + MasterScore;
		CurrentHealth = StartingHealth;
	}
	
	public void UpdateScore(int amount){
		MasterScore = MasterScore + amount;
		ScoreText.text = "Score: " + MasterScore;
	
	}

	public void UpdateHealth(int amount){
		CurrentHealth = CurrentHealth - amount;
		PlayerHealthBar.value = CurrentHealth;
		if (CurrentHealth <= 0) {
			Death ();
		}
	}

	void Death(){
	   SceneManager.LoadScene ("levile001");
	}
}
