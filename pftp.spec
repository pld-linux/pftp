Summary:	fast data transfer program
Summary(pl):	program do szybkiego transferu plik�w
Name:		pftp
Version:	1.1.6
Release:	1
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia
License:	GPL
# native URL is http: but we probaably prefer ftp:
# Source0:	http://pftp.prz.tu-berlin.de/%{name}-%{version}.tar.gz
Source0:	ftp://metalab.unc.edu/pub/Linux/system/network/file-transfer/%{name}-%{version}.tar.gz
URL:		http://star.trek.org/~pftp/
Vendor:		Ben Schluricke <pftp@star.trek.org>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program transfers data from host to host on command line (within
your telnet sessions). You may copy directories recursively,
send/receive stdin/stdout, use your own filters, set net buffer size,
set bandwidth, accept specified clients, start pftp as a daemon, let
inetd start pftp, send files and directories (including a message
file) to other people on the net, manage the data, test the net
performance, send/receive AUDIO and VIDEO streams via UDP unicasted,
broadcasted, and multicasted etc. pftp supports IPv4 as well as
IPv6/IPng with all of the above mentioned features.

%description -l pl
Ten program przesy�a dane z jednego hosta na inny. Jest uruchamiany z
lini komend. Mo�esz kopiowa� katalowi rekursywnie, wysy�a�/odbiera�
standardowy strumie� wej�cia/wyj�cia, u�ywa� w�asnych filtr�w,
ustawia� bufor sieciowy, ustawia� pasmo, akceptowa� okre�lonych
klient�w, startowa� pftp jako serwer, pozwala� by inetd startowa�
pftp, wysy�a� pliki i katalogi (��czenie z plikiem wiadomo�ci) do
innych ludzi z sieci, zarz�dza� danymi, testowa� jako�� sieci,
wysy�a�/odbiera� dane AUDIO oraz WIDEO poprzez UDP unicast, broadcast,
multicast itd. pftp wspiera zar�wno IPv4 jak i IPv6/IPng.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_sysconfdir}}
%{__make} install \
	PREFIX="$RPM_BUILD_ROOT" \
	BINDIR="$RPM_BUILD_ROOT%{_bindir}" \
	MANDIR="$RPM_BUILD_ROOT%{_mandir}"

install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf CREDITS README INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
