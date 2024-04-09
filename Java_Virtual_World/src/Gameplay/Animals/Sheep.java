package Gameplay.Animals;

import Gameplay.Organism;

public class Sheep extends Animal {
    public static final int STRENGTH = 4;
    public static final int INITIATIVE = 4;

    public Sheep(int x, int y) {
        super(x, y, STRENGTH, INITIATIVE);
    }
    @Override
    public String Draw(){
        return "🐑";
    }
    @Override
    public Organism Copy(){
        return new Sheep(x,y);
    }
    @Override
    public String toString(){
        return "Sheep";
    }

}
