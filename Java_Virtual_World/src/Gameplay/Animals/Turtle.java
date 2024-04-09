package Gameplay.Animals;

import Gameplay.Organism;
import java.lang.Math;

public class Turtle extends Animal{
    public static final int STRENGTH = 2;
    public static final int INITIATIVE = 1;
    public static final double PROBABILITY = 0.25;

    public Turtle(int x, int y){
        super(x ,y , STRENGTH, INITIATIVE);
    }

    @Override
    public void Action(){
        if(Math.random() < PROBABILITY){
            randomMove(1);
        }
    }
    @Override
    public boolean didBlocked(Organism opponent){
        return opponent.getStrength() < strength;
    }
    @Override
    public String Draw(){
        return "🐢";
    }
    @Override
    public Organism Copy(){
        return new Turtle(x,y);
    }
    @Override
    public String toString(){
        return "Turtle";
    }
}
