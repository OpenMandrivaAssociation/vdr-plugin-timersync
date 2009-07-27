
%define plugin	timersync
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	9

Summary:	VDR plugin: Synchronize timers with server
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-timersync/
Source:		http://phivdr.dyndns.org/vdr/vdr-timersync/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
