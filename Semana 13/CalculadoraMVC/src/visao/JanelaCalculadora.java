package visao;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import java.awt.FlowLayout;
import javax.swing.BoxLayout;
import javax.swing.JTextField;
import javax.swing.JLabel;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.Dimension;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class JanelaCalculadora extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textFieldNum1;
	private JTextField textFieldNum2;
	private JButton btnSoma;
	private JButton btnLimpar;
	
	
	

	public JButton getBtnSoma() {
		return btnSoma;
	}

	public void setBtnSoma(JButton btnSoma) {
		this.btnSoma = btnSoma;
	}

	public JButton getBtnLimpar() {
		return btnLimpar;
	}

	public void setBtnLimpar(JButton btnLimpar) {
		this.btnLimpar = btnLimpar;
	}

	public JTextField getTextField() {
		return textField;
	}

	public void setTextField(JTextField textField) {
		this.textField = textField;
	}

	public JTextField getTextFieldNum1() {
		return textFieldNum1;
	}

	public void setTextFieldNum1(JTextField textFieldNum1) {
		this.textFieldNum1 = textFieldNum1;
	}

	public JTextField getTextFieldNum2() {
		return textFieldNum2;
	}

	public void setTextFieldNum2(JTextField textFieldNum2) {
		this.textFieldNum2 = textFieldNum2;
	}

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					JanelaCalculadora frame = new JanelaCalculadora();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public JanelaCalculadora() {
		setTitle("Somador");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		
		JPanel panelNorth = new JPanel();
		contentPane.add(panelNorth, BorderLayout.NORTH);
		panelNorth.setLayout(new BoxLayout(panelNorth, BoxLayout.X_AXIS));
		
		textField = new JTextField();
		textField.setPreferredSize(new Dimension(6, 40));
		textField.setMinimumSize(new Dimension(6, 40));
		textField.setFont(new Font("Tahoma", Font.BOLD, 18));
		panelNorth.add(textField);
		textField.setColumns(10);
		
		JPanel panelCenter = new JPanel();
		contentPane.add(panelCenter, BorderLayout.CENTER);
		
		JLabel lblPrimeiroNmero = new JLabel("Primeiro n\u00FAmero: ");
		lblPrimeiroNmero.setFont(new Font("Tahoma", Font.PLAIN, 18));
		panelCenter.add(lblPrimeiroNmero);
		
		textFieldNum1 = new JTextField();
		panelCenter.add(textFieldNum1);
		textFieldNum1.setColumns(15);
		
		JLabel lblSegundoNmero = new JLabel("Segundo n\u00FAmero: ");
		lblSegundoNmero.setFont(new Font("Tahoma", Font.PLAIN, 18));
		panelCenter.add(lblSegundoNmero);
		
		textFieldNum2 = new JTextField();
		panelCenter.add(textFieldNum2);
		textFieldNum2.setColumns(15);
		
		JPanel panelSouth = new JPanel();
		FlowLayout flowLayout = (FlowLayout) panelSouth.getLayout();
		flowLayout.setAlignment(FlowLayout.LEFT);
		contentPane.add(panelSouth, BorderLayout.SOUTH);
		
		btnSoma = new JButton("Somar");
		btnSoma.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		panelSouth.add(btnSoma);
		
		btnLimpar = new JButton("Limpar");
		btnLimpar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
		
			}
		});
		panelSouth.add(btnLimpar);
	}

}
