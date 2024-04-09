package Gameplay.Animals;

import Gameplay.Organism;
import java.lang.Math;
import java.util.Vector;

public abstract class Animal extends Organism {
    public Animal(int x, int y, int s, int i){
        super(x, y, s, i);
    }
    private int prevX;
    private int prevY;
    private boolean didMultiply;

    @Override
    public void Action(){
        randomMove(1);
    }
    @Override
    public void Collision(){
        Organism tmp = world.getCollisionOrg(this);
        if(tmp != null){
            if(tmp.toString().equals(toString())){
                multiply((Animal) tmp);
            }
            else{
                fight(tmp);
            }
        }
    }
    @Override
    public void NextRound(){
        didMultiply = false;
    }
    protected void randomMove(int range){
        if(isSmelling() && areEveryoneStronger()) { return; }

        int[] cords = {-1 * range, 0, range};
        int randomX = cords[(int) (Math.random()*3)];
        int randomY = cords[(int) (Math.random()*3)];
        while ((randomX + x == x && randomY + y == y)
            || !world.isInsideMap(x + randomX, y + randomY)
            || (isSmelling() && world.isOrganismAt(x + randomX, y + randomY) != null && world.isOrganismAt(x + randomX, y + randomY).getStrength() > strength)
        ){
             randomX = cords[(int) (Math.random() * 3)];
             randomY = cords[(int) (Math.random() * 3)];
        }
            changeLocation(x+randomX, y+randomY);
            return;
    }
    protected void changeLocation(int x, int y){
        if(world.isInsideMap(x,y)) {
            prevX = this.x;
            prevY = this.y;
            this.x = x;
            this.y = y;
        }
    }
    private boolean areEveryoneStronger() {
        if(world.isOrganismAt(x-1, y) != null){
            Organism tmp = world.isOrganismAt(x-1, y);
            if(tmp.getStrength() <= strength){ return false; }
        }
        if(world.isOrganismAt(x+1, y) != null){
            Organism tmp = world.isOrganismAt(x+1, y);
            if(tmp.getStrength() <= strength){ return false; }
        }
        if(world.isOrganismAt(x, y - 1) != null){
            Organism tmp = world.isOrganismAt(x, y - 1);
            if(tmp.getStrength() <= strength){ return false; }
        }
        if(world.isOrganismAt(x, y + 1) != null){
            Organism tmp = world.isOrganismAt(x, y + 1);
            if(tmp.getStrength() <= strength){ return false; }
        }

        return true;
    }
    private void reverse(){
        x = prevX;
        y = prevY;
    }
    private void multiply(Animal crush) {
        if(crush.getAge() == 0){ return; }

        Organism child = Copy();
        reverse();
        Vector<Integer> cords = world.getFreeSquare(crush.getX(), crush.getY());
        if((cords.get(0) == crush.getX() && cords.get(1) == crush.getY()) || didMultiply || crush.didMultiply){ return; }

        child.setX(cords.get(0));
        child.setY(cords.get(1));
        world.addOrg(child);
        didMultiply = true;
        crush.didMultiply = true;
    }
    private void fight(Organism opponent){
        if(escape() || opponent.escape()){ return; }
        if(opponent.didBlocked(opponent)){ reverse(); return; }
        if(strength < opponent.getStrength()){
            kill();
            world.getNots().addNode(opponent.toString() + "has killed" + toString() + "at (" + x + "," + y + ")" );
        }
        else{
            opponent.kill();
            world.getNots().addNode(toString() + "has killed" + opponent.toString() + "at (" + x + "," + y + ")" );
        }
    }
}
