package Gameplay;
import java.awt.*;
import java.util.Vector;

abstract public class Organism {
    protected int x;
    protected int y;
    protected int strength;
    protected int initiative;
    protected int age = 0;
    protected boolean alive = true;
    protected World world;

    protected Organism(int x, int y, int strength, int initiative) {
        this.x = x;
        this.y = y;
        this.strength = strength;
        this.initiative = initiative;
    }

    //Setters
    public void setX(int x){
        this.x = x;
    }
    public void setY(int y){
        this.y = y;
    }
    public void setStrength(int s){
        strength = s;
    }
    public void setInitiative(int i){
        initiative = i;
    }
    public void setAge(int a){
        age = a;
    }
    public void setWorld(World w){
        world = w;
    }

    //Getters
    public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }
    public int getStrength(){
        return strength;
    }
    public int getInitiative(){
        return initiative;
    }
    public int getAge(){
        return age;
    }
    public boolean isAlive(){
        return alive;
    }

    public void kill(){
    world.getNots().addNode(toString() + "is dead");
    alive = false;
    }

    public boolean didBlocked(Organism opponent){
        return false;
    }
    public boolean isSmelling(){
        return false;
    }
    public boolean didEscape(){
        return false;
    }
    public boolean escape(){
        if(didEscape()){
            Vector<Integer> tmp = world.getFreeSquare(x, y);

            if(!(tmp.get(0) == x && tmp.get(1) == y)){
                x = tmp.get(0);
                y = tmp.get(1);
                return true;
            }
        }
        return false;
    }
    public void nextYear(){
        age++;
    }

    public abstract void Action();
    public abstract void Collision();
    public abstract String Draw();
    public abstract void NextRound();
    public abstract Organism Copy();
    @Override
    abstract public String toString();
}
