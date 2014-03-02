
package lt.andro.gcm4public;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Spinner;
import android.widget.Toast;

import java.util.HashMap;
import java.util.Map;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.CoreConnectionPNames;
import org.apache.http.params.HttpParams;

import com.fourspaces.couchdb.Database;
import com.fourspaces.couchdb.Document;
import com.fourspaces.couchdb.Session;

/**
 * This is a demo application of GCM4Public open-source project.<br/>
 * <br/>
 * How to create this application, please visit
 * http://www.andro.lt/2012/11/google-cloud-messaging-for-android.html or the project's page:
 * gcm4public.appspot.com
 * 
 * @author Vilius Kraujutis viliusk@gmail.com
 */
public class GCM4PublicDemoActivity extends Activity {

    private static final String TAG = GCM4PublicDemoActivity.class.getSimpleName();

    static String hometown="";
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
      
    
        final Spinner spinner1;
        
       
        	spinner1 = (Spinner) findViewById(R.id.spinner1);
        	spinner1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {

                public void onItemSelected(AdapterView<?> arg0, View arg1,
                        int arg2, long arg3) {
                    //checkOffersSum(); // same method for first 4 spinners. for last 4 spinners is checkScoresSum()

                	 hometown=spinner1.getSelectedItem().toString();
                	
                }

                @Override
                public void onNothingSelected(AdapterView<?> arg0) {
                    // TODO Auto-generated method stub.

                }

            });
        
        
        
        
        String l="";
Log.e("hdbsfjh","dsgfj");
        useExtras();

        GCMIntentService.registerAtGCM(this);
        Log.e("aaaa","dsgfj");
        SharedPreferences prefs = this.getSharedPreferences(
        	      "se.msc.android.droidcouch", Context.MODE_PRIVATE);
      l = prefs.getString("reg", new String());
      Log.e("bbbb","dsgfj");
     // Toast.makeText(this, l, Toast.LENGTH_LONG).show();
      
      
     /* 
      try {
         // HttpPut httpPutRequest = new HttpPut("https://blood.iriscouch.com:5984/" + "preger");
    	  HttpPut httppostRequest = new HttpPut("lnbharath.com/test.php");
          StringEntity body = new StringEntity("{\"FirstName\":\"Isabella\"", "utf8");
          httppostRequest.setEntity(body);
          httppostRequest.setHeader("Accept", "application/json");
          httppostRequest.setHeader("Content-type", "application/json");
          // timeout params
          HttpParams params = httppostRequest.getParams();
          params.setParameter(CoreConnectionPNames.CONNECTION_TIMEOUT, Integer.valueOf(1000));
          params.setParameter(CoreConnectionPNames.SO_TIMEOUT, Integer.valueOf(1000));
          httppostRequest.setParams(params);

        HttpResponse htr=(HttpResponse)new DefaultHttpClient().execute(httppostRequest);
        Log.d("jhfhgd","hfhf");
     //     return jsonResult.getString("rev");
   } catch (Exception e) {
          e.printStackTrace();
   }*/
      
      
    }

    private void useExtras() {
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            String title = extras.getString("title");
            String message = extras.getString("message");
            String url = extras.getString("url");

            if (url != null && !"".equalsIgnoreCase(url)) {
                Uri uri = Uri.parse(url);
                String text = title + "\n" + message;
                if (text.length() != 1) {
                 //   Toast.makeText(getApplicationContext(), text, Toast.LENGTH_LONG).show();
                }
                startActivity(new Intent(Intent.ACTION_VIEW, uri));
            }
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }

    public void openUrl(View v) {
        Uri uri = Uri.parse("https://gcm4public.appspot.com");
        startActivity(new Intent(Intent.ACTION_VIEW, uri));
    }

}
