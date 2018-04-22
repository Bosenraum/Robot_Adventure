package com.example.drewb.finalproject;

import android.os.Bundle;
import android.os.Message;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;


/**
 * Created by Drew on 4/2/2018.
 */

public class Receive implements Runnable {
    ServerSocket server;
    Socket socket;
    BufferedReader input;
    TTS tts;

    public Receive(Socket socket, TTS tts) {
        this.tts = tts;
        this.socket = socket;
    }

    @Override
    public void run() {
            try {
                input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                while(true) {
                    String rec = input.readLine();
                    //System.out.println("Received " + rec);


                    if (rec != null) {
                        if (rec.equals("0:0:STT")) {
                            Message toSTT = MainActivity.handler.obtainMessage();
                            Bundle n = new Bundle();
                            n.putString("main", rec);
                            toSTT.setData(n);
                            MainActivity.handler.sendMessage(toSTT);

                        } else {
                            Message msg = tts.handler.obtainMessage();
                            Bundle b = new Bundle();
                            b.putString("TT", rec);
                            msg.setData(b);
                            tts.handler.sendMessage(msg);
                        }
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
}
