package Gameplay.Animals;

import Gameplay.Organism;

public class Wolf extends Animal{
    public static final int STRENGTH = 9;
    public static final int INITIATIVE = 5;

    public Wolf(int x, int y){
        super(x ,y , STRENGTH, INITIATIVE);
    }
    @Override
    public String Draw(){
        return "🐺";
    }
    @Override
    public Organism Copy(){
        return new Wolf(x,y);
    }
    @Override
    public String toString(){
        return "Wolf";
    }
}
