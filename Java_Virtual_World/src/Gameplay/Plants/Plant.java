package Gameplay.Plants;

import Gameplay.Organism;
import java.lang.Math;
import java.util.Vector;

public abstract class Plant extends Organism {
    static final int INITIATIVE = 0;
    static final double PROBABILITY = 0.1;

    public Plant(int x, int y, int s){
        super(x, y, s, INITIATIVE);
    }

    protected void spread(){
        if(Math.random() < PROBABILITY){
            Vector<Integer> tmp = world.getFreeSquare(x, y);
            if(!(tmp.get(0) == x && tmp.get(1) == y)){
                Organism o = Copy();
                o.setAge(0);
                o.setX(tmp.get(0));
                o.setY(tmp.get(1));
                world.addOrg(o);
            }
        }
    }

    @Override
    public void Action(){
        spread();
    }

    @Override
    public void Collision(){

    }
    @Override
    public void NextRound(){

    }
}
