from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div style='background:blue'><h1><center>JAVA<p>JAVA stands for Just Another Virtual Accelerator. It is a computer-based programming language that is used as a platform in itself. JAVA is an object-oriented, network-centric programming language for programming any mobile apps as well as software.Java was created at Sun Microsystems, Inc., where James Gosling led a team of researchers in an effort to create a new language that would allow consumer electronic devices to communicate with each other. Work on the language began in 1991, and before long the team's focus changed to a new niche, the World Wide Web.</p></center></h1></div>"
if __name__=='__main__':
    app.run(debug=True)