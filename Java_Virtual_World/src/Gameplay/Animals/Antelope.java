package Gameplay.Animals;

import Gameplay.Organism;
import java.lang.Math;

public class Antelope extends Animal {
    public static final int STRENGTH = 4;
    public static final int INITIATIVE = 4;
    public static final int RANGE = 2;
    public static final double PROBABILITY = 0.5;

    public Antelope(int x, int y){
        super(x ,y , STRENGTH, INITIATIVE);
    }

    @Override
    public void Action(){
        randomMove(RANGE);
    }
    @Override
    public boolean didEscape(){
        return Math.random() < PROBABILITY;
    }
    @Override
    public String Draw(){
        return "🦌";
    }
    @Override
    public Organism Copy(){
        return new Antelope(x,y);
    }
    @Override
    public String toString(){
        return "Antelope";
    }
}
