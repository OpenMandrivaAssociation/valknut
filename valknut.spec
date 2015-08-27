Name:		valknut
Version:	0.4.9
Release:	3
Summary:	QT based Direct Connect file sharing client
Group:		Networking/File transfer
License:	GPLv2+ and LGPLv3+
URL:		http://sourceforge.net/projects/wxdcgui/
Source0:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
Source1:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}-oxygen-icons.tar.gz
Source2:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}-gnome-icons.tar.gz
Source3:	valknut.desktop
Patch0:		valknut-0.4.9-fix-_exit-undefined-error.patch
BuildRequires:	dc-devel >= 0.3.23
BuildRequires:	qt4-devel >= 4.3.0
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	desktop-file-utils
Obsoletes:	dcgui

%description
This is a client for the Direct Connect file sharing protocol with a nice
GUI. It is compatible with other DC clients, such as the original DC from
Neomodus, DC++ and derivatives. It also inter-operates with all common DC
hub software.
This is QT4 version imported from MIB. PLF QT3 version is no longer supported.


%prep
%setup -qn %{name}-%{version}
%patch0 -p1

%build
%configure2_5x --enable-mt
%make


%install
%makeinstall_std


# Install oxygen icon theme
tar xzf %{SOURCE1} -C %{buildroot}%{_datadir}/%{name}/icons/appl
# Install gnome icons theme
tar xzf %{SOURCE2} -C %{buildroot}%{_datadir}/%{name}/icons/appl

# Remove the provided .desktop file
rm %{buildroot}%{_datadir}/applications/valknut.desktop
# and install our own
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE3}


%files
%doc AUTHORS ChangeLog COPYING COPYING.OpenSSL INSTALL README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
# More concise?
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*
