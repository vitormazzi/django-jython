Requierments:

You'll need a lot of JAR files on your CLASSPATH for JNDI lookups to
work 

These JAR files were obtained from the Glassfish v2.1.1 binary install
for Linux.

    appserv-admin.jar
    appserv-deployment-client.jar
    appserv-ext.jar
    appserv-launch.jar
    appserv-rt.jar
    imqjmsra.jar
    j2ee.jar
    javaee.jar

The imqjmsra.jar file is located under  the
GLASSFISH_HOME/lib/install/applications/jmsra directory.  I have no
idea why you have to have JMS installed to get JNDI lookups for JDBC.

For Postgresql JDBC support  - I use:

    postgresql-8.3-604.jdbc4.jar


Once all that is working, the following raw DBAPI/zxJDBC code should
bind you into the JDBC connection pool with a JNDI name of
'jdbc/pgpool-demo' as configured in the Jython book.

    from __future__ import with_statement
    from contextlib import closing
    from com.ziclix.python.sql import zxJDBC
    from javax.naming import Context

    # This specifies the Glassfish ContextFatory class and the 
    # CORBA IIOP host and port
    props = {'com.sun.appserv.iiop.endpoints': 'localhost:3700',
              Context.INITIAL_CONTEXT_FACTORY: "com.sun.appserv.naming.S1ASCtxFactory"}

    jndiName = 'jdbc/pgpool-demo'
    with closing(zxJDBC.lookup(jndiName, **props)) as con:
        print con

