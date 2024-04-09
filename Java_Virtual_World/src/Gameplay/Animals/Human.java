package Gameplay.Animals;

import Gameplay.Organism;
import java.lang.Math;

public class Human extends Animal {
    public static final int STRENGTH = 5;
    public static final int INITIATIVE = 4;
    public static final int ABILITY = 5;
    private int specialRounds = 0;

    public Human(int x, int y){
        super(x ,y , STRENGTH, INITIATIVE);
    }

    @Override
    public void Action(){

    }
    @Override
    public String Draw(){
        return "🧍‍♂️";
    }
    @Override
    public Organism Copy(){
        return new Human(x,y);
    }
    @Override
    public String toString(){
        return "Human";
    }
    public int getSpecialRounds(){
        return specialRounds;
    }
    public void setSpecialRounds(int s){
        specialRounds = s;
    }
}
