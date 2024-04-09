package Gameplay;
import java.util.Vector;
public class Notifications {
    final private Vector<String> nots;
    public Notifications(){
        nots = new Vector<String>();
    }
    public void addNode(String node){
        nots.add(node);
    }
    public void clearNots(){
        nots.clear();
    }
    public String loadNots(){
        StringBuilder out = new StringBuilder();
        for(String node : nots){
            out.append(node).append("\n");
        }
        return out.toString();
    }
}
