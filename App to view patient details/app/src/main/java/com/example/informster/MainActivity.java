package com.example.informster;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.ResultReceiver;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MainActivity extends AppCompatActivity {
    private String unique_id ;
    private String password;
    private String Hospital_name;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button submit = (Button) findViewById(R.id.Submit);
        EditText unique_id_field =  (EditText) findViewById(R.id.UID);
        EditText pwd_field = (EditText) findViewById(R.id.Pwd);
        EditText hospital_name_field =  (EditText) findViewById(R.id.Hospital);
        TextView Status =  findViewById(R.id.Status_Bar);
        Status.setText("");


        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("Error", "onClick: Clicked");
                Status.setText("Button Clicked");
                Log.d("Error", "Text changed");
                unique_id=  unique_id_field.getText().toString();
                Hospital_name =  hospital_name_field.getText().toString();
                password =  pwd_field.getText().toString();

                Connection con =  Connect.getConnection(Hospital_name);
                if (con!=null) {
                    Status.setText("Connected to the database");
                    String q = "Select Uniqueid from Patient_info";
                    if (Hospital_name.length() > 0)
                    {
                        try {
                            String uid_correct =  MainActivity.uid_exists(unique_id,q,con);
                            if (uid_correct!=null) {
                                Log.d("Test", "onClick: The uid found is " + unique_id);
                                boolean correct_password =  MainActivity.check_password(password,uid_correct, con);
                                if(correct_password)
                                {
                                    Status.setText("The Password is correct");
                                    Intent intent = new Intent(getApplicationContext(), HeartRate.class);
                                    intent.putExtra("uid",uid_correct);
                                    intent.putExtra("Hospital_name",Hospital_name);
                                    startActivity(intent);
                                }
                                else
                                {
                                    Log.e("TAG", "onClick: The password is incorrect" );
                                    Status.setText("The password is incorrect");
                                }
                            }
                            else
                            {
                                Status.setText("The value is not found");
                            }
                        } catch (SQLException throwables) {
                            throwables.printStackTrace();
                        }
                    }
                }
                else
                {
                    Status.setText("mhhhhh");
                }
            }

        });
    }
    private static String uid_exists (String unique_id, String q ,  Connection con) throws SQLException {
        Statement st =  con.createStatement();
        ResultSet set  =  st.executeQuery(q);
        String id = null;
        boolean value_exists =  false;

        while(set.next())
        {
            String uid =  set.getString(1);
            if (uid.equalsIgnoreCase(unique_id))
            {
                return uid;
            }
        }
        return null;
    }
    private static boolean check_password(String Password, String uid ,  Connection con) throws SQLException {
        Log.d("check pass", "check_password:In connect password ");
        String q  =  "Select Pass from " + uid + " where Srno=1";
        PreparedStatement pstsmt =  con.prepareStatement(q);
        ResultSet set =  pstsmt.executeQuery();
        while (set.next())
        {
            String pass  =  set.getString(1);
            if(Password.equals(pass))
            {
                return  true;
            }
            else
            {
                return false;
            }
        }
        return  false;
    }
}