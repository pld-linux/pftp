Summary:	fast data transfer program
Summary(pl):	program do szybkiego transferu plików
Name:		pftp
Version:	1.1.6
Release:	2
License:	GPL
Vendor:		Ben Schluricke <pftp@star.trek.org>
Group:		Networking/Utilities
# native URL is http: but we probaably prefer ftp:
# Source0:	http://pftp.prz.tu-berlin.de/%{name}-%{version}.tar.gz
Source0:	ftp://metalab.unc.edu/pub/Linux/system/network/file-transfer/%{name}-%{version}.tar.gz
URL:		http://star.trek.org/~pftp/
Conflicts:	ftp-pftp
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
Ten program przesy³a dane z jednego hosta na inny. Jest uruchamiany z
linii poleceñ. Pozwala na rekurencyjnie kopiowanie katalogów,
wysy³anie/odbieranie standardowego strumienia wej¶ciowego/wyj¶ciowego,
u¿ywanie w³asnych filtrów, ustawienie bufora sieciowego, ustawienie
pasma, akceptowanie okre¶lonych klientów, umo¿liwia uruchamianie pftp
jako demona, uruchamianie go przez inetd, przesy³anie plików i
katalogów (do³±czaj±c plik komunikatu) do innych osób w sieci,
zarz±dzanie danymi, testowanie wydajno¶ci sieci, wysy³anie/odbieranie
strumieni d¼wiêkowych i wizyjnych po UDP w trybie unicastowym,
broadcastowym i multicastowym itd. pftp wspiera zarówno IPv4 jak i
IPv6/IPng.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README INSTALL
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
