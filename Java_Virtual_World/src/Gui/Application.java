package Gui;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.*;

public class Application extends JFrame {
        public static final String title = "Patryk Miszke 193249 Virtual World V1.0";

        public Application(){
            setTitle(title);
            setSize(900, 700);
            setLocationRelativeTo(null);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            Panel();

            setVisible(true);
        }

        public void Panel() {
            JPanel notifications = new JPanel();
            JLabel N = new JLabel("Notifications");
            notifications.add(N);
            notifications.setBackground(Color.PINK);

            JSplitPane splitIt = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT);
            splitIt.setRightComponent(notifications);
            JPanel board = createBoard();
            splitIt.setLeftComponent(board);
            splitIt.setDividerSize(0);
            splitIt.setDividerLocation(650);
            add(splitIt);
            validate();
        }

    public JPanel createBoard() {
        JPanel board = new JPanel(new GridLayout(20, 20));
        ImageIcon icon = new ImageIcon("src/empty.png");
        for (int i = 0; i < 400; i++) {
            JLabel label = new JLabel(new ImageIcon(icon.getImage()));
            board.add(label);
        }
        board.setPreferredSize(new Dimension(600, 600));
        return board;
    }
}
