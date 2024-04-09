import Gui.Application;
import javax.swing.SwingUtilities;
import java.sql.SQLOutput;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Application app = new Application();
        });
    }
}
