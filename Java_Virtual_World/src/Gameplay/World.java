package Gameplay;

import java.util.Vector;
public class World {
        private int height;
        private int width;
        private Move move = Move.Stand;
        private  int round;
        private Notifications nots;
        Vector<Organism> organisms;

        public World(int height, int width){
                this.height = height;
                this.width = width;
                organisms = new Vector<Organism>();
                nots = new Notifications();
        }

        //Setters
        public void setRound(int r){ round = r; }
        public void setMove(Move m){ move = m; }

        //Getters
        public int getHeight(){ return height; }
        public int getWidth(){ return width; }
        public Notifications getNots(){ return nots; }
        public int getRound(){ return round; }
        public Move getMove(){ return move; }
        public Vector<Organism> getOrganisms(){ return organisms; }

        public enum Move{
                Up,
                Down,
                Right,
                Left,
                Stand,
                Ult
        }
        public Move popMove(){
                Move m = move;
                move = Move.Stand;
                return m;
        }
        public boolean isInsideMap(int x, int y){ return x < width && x >= 0 && y < height && y >= 0; }
        public Organism isOrganismAt(int x, int y){
                Organism wanted = null;
                for(Organism tmp : organisms){
                        if(tmp.getX() == x && tmp.getY() == y && tmp.isAlive()){
                                if(wanted == null || wanted.getStrength() < tmp.getStrength()){
                                        wanted = tmp;
                                }
                        }
                }
                return wanted;
        }
        public Vector<Integer> getFreeSquare(int x, int y){
                for(int i = -1; i <= 1; i++){
                        for(int j = -1 ; j <= 1 ; j++){
                                Vector<Integer> v = new Vector<Integer>();
                                v.add(x+i);
                                v.add(y+j);
                                if(!(v.get(0) == x && v.get(1) == y)
                                && isInsideMap(v.get(0), v.get(1))
                                && isOrganismAt(v.get(0), v.get(1)) == null
                                ){
                                        return v;
                                }
                        }
                }
                Vector<Integer> failed = new Vector<Integer>();
                failed.add(x);
                failed.add(y);
                return failed;
        }
        public Organism getCollisionOrg(Organism o){
                for(Organism tmp : organisms){
                        if(o.getX() == tmp.getX() && o.getY() == tmp.getY()
                        && o != tmp
                        && o.isAlive()
                        ){
                                return tmp;
                        }
                }
                return null;
        }
        private void newRoundInfo(){
                nots.clearNots();
                for(Organism tmp : organisms){
                        tmp.NextRound();
                }
        }
        private void clearMap(){
                for(Organism tmp : organisms){
                        if(!tmp.isAlive()){
                                organisms.remove(tmp);
                                clearMap();
                                break;
                        }
                }
        }
        private void actions(){
                organisms.sort((Organism tmp, Organism tmp2) -> {
                       if(tmp.getInitiative() == tmp2.getInitiative()){
                               return tmp2.getAge() - tmp.getAge();
                       }
                       return tmp2.getAge() - tmp.getAge();
                });
                for(Organism tmp : organisms){
                        if(tmp.isAlive()){
                                tmp.Action();
                                tmp.Collision();
                        }
                        tmp.nextYear();
                }
        }


        public void runRound(){
                newRoundInfo();
                round++;
                actions();
                clearMap();
        }
        public void addOrg(Organism o){
                o.setAge(o.getAge()+1);
                o.setWorld(this);
                organisms.add(o);
        }
}
