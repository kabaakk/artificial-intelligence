using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Speech.Synthesis;
using System.Speech.Recognition;
using System.Diagnostics;

namespace yapay_zeka
{
    public partial class Form1 : Form
    {
        SpeechSynthesizer s = new SpeechSynthesizer();
        public Form1()
        {
            InitializeComponent();
            SpeechRecognitionEngine reco = new SpeechRecognitionEngine();
            Choices list = new Choices();

            s.SpeakAsync("hoşgeldiniz efendim");

            list.Add(new string[] { "merhaba", "nasılsın","internet","video","mozilla","bye","kapat","napıyorsun" });

            Grammar gm = new Grammar(new GrammarBuilder(list));

            try
            {
                reco.RequestRecognizerUpdate();
                reco.LoadGrammar(gm);
                reco.SpeechRecognized += Reco_SpeechRecognized;
                reco.SetInputToDefaultAudioDevice();
                reco.RecognizeAsync(RecognizeMode.Multiple);
            } catch { }
        }

        private void Reco_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            
            string a = e.Result.Text;

            switch (a)
            {
                case ("merhaba"):
                    s.SpeakAsync("merhaba");
                    break;
                case ("nasılsın"):
                    s.Speak("iyiyim sen nasılsın");
                    break;
                case ("napıyorsun"):
                    s.Speak("sizi bekliyorum siz napıyorsunuz");
                    break;
                case ("internet"):
                    s.Speak("google geliyor");
                    Process.Start("https://www.google.com");
                    break;
                case ("mozilla"):
                    s.Speak("mozilla geliyor");
                    Process.Start("firefox.exe");
                    break;
                case ("video"):
                    s.Speak("youtube geliyor");
                    Process.Start("https://www.youtube.com");
                    break;
                case ("kapat"):
                    SendKeys.Send("%{F4}");
                    break;
                case ("bye"):
                    s.Speak("görüşürüz efendim iyi günler");
                    this.Close();
                    break;

              }
         }
    }
}
