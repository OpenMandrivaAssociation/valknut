Name:		valknut
Version:		0.4.9
Release:		3
Summary:		QT based Direct Connect file sharing client
Group:		Networking/File transfer
License:		GPLv2+ and LGPLv3+
URL:		http://sourceforge.net/projects/wxdcgui/
Source0:		http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
Source1:		http://dl.sourceforge.net/wxdcgui/%{name}-%{version}-oxygen-icons.tar.gz
Source2:		http://dl.sourceforge.net/wxdcgui/%{name}-%{version}-gnome-icons.tar.gz
Source3:		valknut.desktop
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
rm -rf %{buildroot}
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



%changelog
* Sun Oct 13 2012 Giovanni Mariani <mc2374@mclink.it> 0.4.9-2
- Corrected the BReq for dclib-devel (now is dc-devel)
- Added P0 to fix error build (_exit fn undefined)

* Sun Aug 07 2011 Andrey Bondrov <abondrov@mandriva.org> 0.4.9-1mdv2012.0
+ Revision: 693578
- imported package valknut

* Tue Dec 28 2010 Giovanni Mariani <mc2374@mclink.it> 0.4.9-69.1mib2010.2
- Ported to Mdv 2010.2 for MIB from an old FC10 package
- Revised Source3 to make it pass the desktop-file-validate test
- Added some version info to BRs
- Made the BuildRoot tag compliant with Wiki specs
- Made use of proper macros instead of the deprecated "$RPM_BUILD_ROOT" one
- Corrected man page compression format
- Corrected .desktop filename

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.4.9-1
- Update to 0.4.9
- Removed gcc4.4 patch (merged upstream)
- Fixed typo in description
- Fixed license tag
- Added oxygen/gnome icons themes as sources

* Wed Feb  4 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.4.8-2
- Added valknut-gcc44.patch to fix the build with gcc 4.4

* Wed Jan 28 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.4.8-1
- Update to 0.4.8
- Switch to QT4
- Removed Source2:valknut.png (part of the source package now)
- Fixed desktop file
- Man pages
- Many bugfixes, code cleanup etc.
- Upload slot changes
- Major feature changes (together with dclib) mentioned in NEWS from 0.4.0 to 0.4.7:
  0.4.6: Segment size adjustable, Download folders from search, Warnings about settings,
  0.4.5: More search results returned, Switching active/passive mode, StrongDC compatible encryption,
  Partial list uploads, Search window improvements, User list icon changes
  0.4.0: Nick tab completion improvements, Chat command improvements, Filelist storage changes, 
  Public hubs display improved, /rebuild command fixed and improved, Folder search results

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> 0.3.11-5
- rebuild with new openssl

* Fri Apr 04 2008 Luke Macken <lmacken@redhat.com> 0.3.11-4
- Add qt3-devel to BuildRequires to fix build issue (#440837)

* Fri Feb  8 2008 Luke Macken <lmacken@redhat.com> 0.3.11-3
- Rebuild for gcc 4.3

* Wed Dec  5 2007 Luke Macken <lmacken@redhat.com> 0.3.11-2
- Rebuild

* Sun Oct 14 2007 Luke Macken <lmacken@redhat.com> 0.3.11-1
- 0.3.11

* Tue Aug 27 2007 Luke Macken <lmacken@redhat.com> 0.3.10-1
- 0.3.10
- Update License to GPLv2

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> 0.3.8.1-1
- 0.3.8.1

* Mon Jan  3 2007 Luke Macken <lmacken@redhat.com> 0.3.8-1
- 0.3.8 from new upstream
- Remove valknut-0.3.7-extra-qualification.patch

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 0.3.7-9
- Rebuild for FC6

* Sun Apr 30 2006 Luke Macken <lmacken@redhat.com> 0.3.7-8
- Execute with --disable-tray in desktop file, since it is horribly broken.

* Tue Feb 28 2006 Luke Macken <lmacken@redhat.com> 0.3.7-7
- Add patch to remove extra qualification build error

* Wed Feb 15 2006 Luke Macken <lmacken@redhat.com> 0.3.7-6
- Rebuild for FE5

* Wed Nov 09 2005 Luke Macken <lmacken@redhat.com> 0.3.7-5
- Rebuild for new openssl

* Tue Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-4
- Add openssl-devel to BuildRequires

* Mon Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-3
- Add bzip2-devel to BuildRequires

* Mon Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-2
- Requires desktop-file-utils
- Use environment variables instead of hardcoding QTDIR
- Remove duplicate category from desktop file
- Use -p when calling 'install'

* Thu Sep 29 2005 Luke Macken <lmacken@redhat.com> 0.3.7-1
- Packaged for Fedora Extras
