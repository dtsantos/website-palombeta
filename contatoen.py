import webapp2
import cgi
from google.appengine.api import users
from google.appengine.api import mail

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("""
      
<!DOCTYPE HTML>
<html>

<head>
  <title>Boat Trips in Paraty/RJ-Brazil</title>
  <meta name="description" content="Take a exclusive tour of the Bay of Paraty on a brand new 16 feet speedboat for up to 4 guests. Fluent english speaking guide. R$ 399/day" />
  <meta name="keywords" content="paraty, speedboat, boat, tour, brazil, beach, island, bay, mamangua, praia vermelha, red beach, ilha comprida, sapeca" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <!-- stylesheets -->
  <link href="css/style.css" rel="stylesheet" type="text/css" />
  <link href="css/dark.css" rel="stylesheet" type="text/css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
</head>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38329051-1']);
  _gaq.push(['_setDomainName', 'palombeta.com']);
  _gaq.push(['_setAllowLinker', true]);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
<body>
  <div id="main">

    <!-- begin header -->
    <header>
      <div id="logo"><h1>Palombeta <a href="#">Speedboat</a></h1></div>
      <nav>
        <ul class="sf-menu" id="nav">
          <li><a href="index.en.html">Home</a></li>
          <li><a href="lancha.en.html">The Speedboat</a></li>
          <li><a href="roteiros.en.html">Destinations</a></li>
          <li><a href="tarifas.en.html">Rates</a></li>
          <li class="selected"><a href="contato.en.html">Contact</a></li>
    	  <li><a href="contato.html"><img src="./images/portugues.gif" width="26" height="18" alt="Portugues" /></a></li>   
    
  </tr>
          
        </ul>
      </nav>
    </header>    <!-- end header -->
    
    <!-- begin content -->
    <div id="site_content">
      <div id="left_content">
        <h1>Contact</h1>
        <p>Please fill the form bellow and we will get in touch with you in no more then 30 minutes:<br>
        
        <form action="/confirmacao.en.html" method="post">
                <table style="margin-left: 3px" width="50%">
 				<tr>
				  <td align="left"><label for="usr">Name:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="nome" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Telephone:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="tel" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">E-mail:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="email" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Message:</label>&nbsp;
				  </td>
  				  <td><textarea name="msg" rows="8" cols="40"></textarea></td>
  				
				  <td></td> 
			 	</tr>
			 	<tr>
			 	 <td>
			 	 </td>
			 	 <td align="center"><input type="submit" value="  Enviar  "></td>
			 	</tr>
				</table>
    	</form>
        </p>
        <p><strong>Telephones:</strong> +55 24 9975-7859 / +55 24 3371-0365<br>
        <strong>E-mail:</strong>  davitrindade@gmail.com</p>
        
      </div>
      <div id="right_content">
        <img src="images/solo.jpg" width="450" height="450" title="contact" alt="contact" />
      </div>
    </div>
    <!-- end content -->

    <!-- begin footer -->
    <footer>
      <p>Speedboat Tours in Paraty, Brazil. (24) 9975-7859.</p>
      <p><img src="images/facebook.png" alt="facebook" />&nbsp;<img src="images/rss.png" alt="rss" /></p>
    </footer>
    <!-- end footer -->

  </div>
  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/jquery.easing-sooper.js"></script>
  <script type="text/javascript" src="js/jquery.sooperfish.js"></script>
  <!-- initialise sooperfish menu -->
  <script type="text/javascript">
    $(document).ready(function() {
      $('ul.sf-menu').sooperfish();
    });
  </script>
</body>	
</html>

      """)
      
class Confirmacao(webapp2.RequestHandler):
    def post(self):
    	message = mail.EmailMessage(sender="Davi Trindade <davitrindade@gmail.com>",
                            subject="Palombeta inquiry: "+self.request.get('nome'),to="davitrindade@gmail.com",
                            body="Sender: "+self.request.get('nome')+"\nTelephone: "+self.request.get('tel')+"\nEmail: "+self.request.get('email')+"\nMessage: \n"+self.request.get('msg'))
	message.send()
	
	self.response.out.write("""
      
<!DOCTYPE HTML>
<html>

<head>
  <title>Boat Trips in Paraty/RJ-Brazil</title>
  <meta name="description" content="Take a exclusive tour of the Bay of Paraty on a brand new 16 feet speedboat for up to 4 guests. Fluent english speaking guide. R$ 399/day" />
  <meta name="keywords" content="paraty, speedboat, boat, tour, brazil, beach, island, bay, mamangua, praia vermelha, red beach, ilha comprida, sapeca" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <!-- stylesheets -->
  <link href="css/style.css" rel="stylesheet" type="text/css" />
  <link href="css/dark.css" rel="stylesheet" type="text/css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
</head>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38329051-1']);
  _gaq.push(['_setDomainName', 'palombeta.com']);
  _gaq.push(['_setAllowLinker', true]);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
<body>
  <div id="main">

    <!-- begin header -->
    <header>
      <div id="logo"><h1>Palombeta <a href="#">Speedboat</a></h1></div>
      <nav>
        <ul class="sf-menu" id="nav">
          <li><a href="index.en.html">Home</a></li>
          <li><a href="lancha.en.html">The Speedboat</a></li>
          <li><a href="roteiros.en.html">Destinations</a></li>
          <li><a href="tarifas.en.html">Rates</a></li>
          <li class="selected"><a href="contato.en.html">Contact</a></li>
    	  <li><a href="contato.html"><img src="./images/portugues.gif" width="26" height="18" alt="Portugues" /></a></li>   
    
  </tr>
          
        </ul>
      </nav>
    </header>    <!-- end header -->
    
    <!-- begin content -->
    <div id="site_content">
      <div id="left_content">
        <h1>Confirmation</h1>
        <p>
        <strong>Thank you for your message!</strong>	<br><br>
        We will get in touch with you in no more then 30 minutes at any day between 9:00 and 14:00 (local Paraty time). 
        At other times we will answer you on the same day.<br><br>
        <br><br><br><br>
        Phone numbers:
        </p>
        <p><strong>Telephones:</strong> +55 24 9975-7859 / +55 24 3371-0365<br>
        <strong>E-mail:</strong>  davitrindade@gmail.com</p>
        
      </div>
      <div id="right_content">
        <img src="images/solo.jpg" width="450" height="450" title="contact" alt="contact" />
      </div>
    </div>
    <!-- end content -->

    <!-- begin footer -->
    <footer>
      <p>Speedboat Tours in Paraty, Brazil. (24) 9975-7859.</p>
      <p><img src="images/facebook.png" alt="facebook" />&nbsp;<img src="images/rss.png" alt="rss" /></p>
    </footer>
    <!-- end footer -->

  </div>
  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/jquery.easing-sooper.js"></script>
  <script type="text/javascript" src="js/jquery.sooperfish.js"></script>
  <!-- initialise sooperfish menu -->
  <script type="text/javascript">
    $(document).ready(function() {
      $('ul.sf-menu').sooperfish();
    });
  </script>
</body>	
</html>

      """)
	

      
app = webapp2.WSGIApplication([('/contato.en.html', MainPage),
                              ('/confirmacao.en.html', Confirmacao)],
                              debug=True)