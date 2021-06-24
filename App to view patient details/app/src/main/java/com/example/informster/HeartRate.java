package com.example.informster;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.TimeUnit;

public class HeartRate extends AppCompatActivity {
    Handler handler=new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_heart_rate);
        Intent intent = getIntent();
        String unique_id = intent.getStringExtra("uid");
        String hopital_name = intent.getStringExtra("Hospital_name");
        TextView Pateint_name =  (TextView) findViewById(R.id.PatientName);
        TextView Room_no = (TextView) findViewById(R.id.Room_no);
        TextView Disease = (TextView) findViewById(R.id.Disease);
        Connection con =  Connect.getConnection(hopital_name);
        TextView pulse = (TextView) findViewById(R.id.Pulse_rate);
        try {
            String name = getName(con,unique_id);
            Pateint_name.setText("Patient name:  " +  name);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        try
        {
            Disease.setText("Reason of Hospitalization :  " + getDisease(con,unique_id));
        }
        catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        try {
            Room_no.setText("Room no : "+ getRoom_no(con,unique_id));
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        Timer timer =  new Timer();
        TimerTask taskk = new TimerTask() {
            @Override
            public void run() {
                String q = "Select Heart_Rate from " + unique_id + " where Srno=(Select max(Srno) from " + unique_id +")";
                PreparedStatement p = null;
                try {
                    p = con.prepareStatement(q);
                    Integer heart_rate = 0;
                    String heart_rate_s = "";
                    ResultSet set = p.executeQuery();
                    while(set.next())
                    {
                        heart_rate_s =  set.getString(1);
                        heart_rate =  Math.round(Float.parseFloat(heart_rate_s));
                        heart_rate_s =  heart_rate.toString();
                        break;
                    }
                    pulse.setText(heart_rate_s);
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
        };
        timer.schedule(taskk,50000,50000);

    }
    public static String getName(Connection con,String uid) throws SQLException {
        String name = "";
        String quuery  =  "Select Name from Patient_info where Uniqueid = ?";
        PreparedStatement pstmt =  con.prepareStatement(quuery);
        pstmt.setString(1,uid);
        ResultSet set =  pstmt.executeQuery();
        while (set.next())
        {
            name =  set.getString(1);
            return name;
        }
        return name;

    }
    public static int getRoom_no(Connection con,String uid) throws SQLException {
        int Room_no = 0;
        String quuery  =  "Select Roomno from Patient_info where Uniqueid = ?";
        PreparedStatement pstmt =  con.prepareStatement(quuery);
        pstmt.setString(1,uid);
        ResultSet set =  pstmt.executeQuery();
        while (set.next())
        {
            Room_no =  set.getInt(1);
            return Room_no;
        }
        return  Room_no;
    }
    public static String getDisease(Connection con,String uid) throws SQLException {
        String Disease = "";
        String quuery  =  "Select Disease from Patient_info where Uniqueid = ?";
        PreparedStatement pstmt =  con.prepareStatement(quuery);
        pstmt.setString(1,uid);
        ResultSet set =  pstmt.executeQuery();
        while (set.next())
        {
            Disease =  set.getString(1);
            return Disease;
        }
        return Disease;

    }


}