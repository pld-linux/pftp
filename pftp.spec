Summary:	fast data transfer program
Summary(pl):	program do szybkiego transferu plików
Name:		pftp
Version:	1.0.15
Release:	1
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Copyright:	GPL
Source: 	http://star.trek.org/~pftp/%{name}-%{version}.tar.gz
Patch:		pftp-config.patch
URL:		http://star.trek.org/~pftp/
Vendor:		Ben Schluricke <pftp@star.trek.org>
#Prereq:         %{_sbindir}/useradd
#Prereq:         %{_sbindir}/groupadd
#Prereq:         %{_sbindir}/userdel
#Prereq:         %{_sbindir}/groupdel
#Prereq:		/bin/hostname
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This program transfers data from host to host on command line
(within your telnet sessions). You may copy directories recursively,
send/receive stdin/stdout, use your own filters, set net buffer
size, set bandwidth, accept specified clients, start pftp as a daemon,
let inetd start pftp, send files and directories (including a message
file) to other people on the net, manage the data, test the net
performance, send/receive AUDIO and VIDEO streams via UDP unicasted,
broadcasted, and multicasted etc. pftp supports IPv4 as well as
IPv6/IPng with all of the above mentioned features.

%description -l pl
Ten program przesy³a dane z jednego hosta na inny. Jest uruchamiany
z lini komend. Mo¿esz kopiowaæ katalowi rekursywnie, wysy³aæ/odbieraæ
standardowy strumieñ wej¶cia/wyj¶cia, u¿ywaæ w³asnych filtrów, ustawiaæ
bufor sieciowy, ustawiaæ pasmo, akceptowaæ okre¶lonych klientów,
startowaæ pftp jako serwer, pozwalaæ by inetd startowa³ pftp, wysy³aæ
pliki i katalogi (³±czenie z plikiem wiadomo¶ci) do innych ludzi z sieci,
zarz±dzaæ danymi, testowaæ jako¶æ sieci, wysy³aæ/odbieraæ dane AUDIO
oraz WIDEO poprzez UDP unicast, broadcast, multicast itd. pftp wspiera
zarówno IPv4 jak i IPv6/IPng.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d 	$RPM_BUILD_ROOT{%{_bindir},%{_mandir},/etc}
make		PREFIX="$RPM_BUILD_ROOT"\
		BINDIR="$RPM_BUILD_ROOT%{_bindir}"\
		MANDIR="$RPM_BUILD_ROOT%{_mandir}" install
install 	%{name}.conf $RPM_BUILD_ROOT/etc
strip		$RPM_BUILD_ROOT%{_bindir}/%{name}
gzip -9nf	$RPM_BUILD_ROOT%{_mandir}/man*/* CREDITS README INSTALL || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CREDITS,README,INSTALL}.gz
%attr(755, root, root) %{_bindir}/%{name}
%config(noreplace) %verify(not size mtime md5) /etc/%{name}.conf
