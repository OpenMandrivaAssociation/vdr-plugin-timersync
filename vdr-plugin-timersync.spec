%define plugin	timersync

Summary:	VDR plugin: Synchronize timers with server
Name:		vdr-plugin-%plugin
Version:	0.1.0
Release:	12
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-timersync/
Source:		http://phivdr.dyndns.org/vdr/vdr-timersync/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	svdrpservice-devel
Requires:	vdr-abi = %vdr_abi
Requires:	vdr-plugin-svdrpservice

%description
This plugin synchronizes timers between client VDR and server VDR.
All recordings are done at server, but all timers are visible in
both VDR instances.

%prep
%setup -q -n %plugin-%{version}
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
%doc README HISTORY


