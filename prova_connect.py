import Pyro4
Host = "192.168.3.180"
ns = Pyro4.naming.locateNS(host = Host)
uri=ns.lookup("CPU_LOAD")
(preuri,posturi) = uri.asString().split(sep="@")
(address, port ) = posturi.split(sep=":")
uri = preuri +"@"+ Host +":" + port
thing = Pyro4.Proxy(uri)
print ("Numero CORE ",thing.get_n_core())
