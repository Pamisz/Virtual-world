package Gameplay.Animals;

import Gameplay.Organism;

public class Fox extends Animal {
    public static final int STRENGTH = 3;
    public static final int INITIATIVE = 7;

    public Fox(int x, int y){
        super(x ,y , STRENGTH, INITIATIVE);
    }

    @Override
    public boolean isSmelling(){
        return true;
    }
    @Override
    public String Draw(){
        return "🦊";
    }
    @Override
    public Organism Copy(){
        return new Fox(x,y);
    }
    @Override
    public String toString(){
        return "Fox";
    }
}
