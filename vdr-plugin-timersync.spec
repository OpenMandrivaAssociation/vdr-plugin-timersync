
%define plugin	timersync
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	10

Summary:	VDR plugin: Synchronize timers with server
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-timersync/
Source:		http://phivdr.dyndns.org/vdr/vdr-timersync/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	svdrpservice-devel
Requires:	vdr-abi = %vdr_abi
Requires:	vdr-plugin-svdrpservice

%description
This plugin synchronizes timers between client VDR and server VDR.
All recordings are done at server, but all timers are visible in
both VDR instances.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

perl -pi -e 's,"../svdrpservice/svdrpservice.h",<vdr/svdrpservice/svdrpservice.h>,' timersync.c

%vdr_plugin_params_begin %plugin
# VDR Server address and optional SVDRP port
# This can also be configured in svdrpservice plugin setup menu
var=VDR_SERVER_ADDRESS
param=--server=VDR_SERVER_ADDRESS
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-9mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-8mdv2009.1
+ Revision: 359377
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-7mdv2009.0
+ Revision: 197989
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-6mdv2009.0
+ Revision: 197735
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-5mdv2008.1
+ Revision: 145229
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-4mdv2008.1
+ Revision: 103224
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-3mdv2008.0
+ Revision: 50058
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2008.0
+ Revision: 42141
- rebuild for new vdr

* Sun Jun 10 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2008.0
+ Revision: 37870
- initial Mandriva release

