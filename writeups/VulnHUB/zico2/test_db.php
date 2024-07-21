<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<!-- Copyright 2023 phpLiteAdmin (http://phpliteadmin.googlecode.com) -->
<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
<title>phpLiteAdmin</title>

<!-- begin the customizable stylesheet/theme -->
<style type="text/css">
/* overall styles for entire page */
body
{
	margin: 0px;
	padding: 0px;
	font-family: Arial, Helvetica, sans-serif;
	font-size: 14px;
	color: #000000;
	background-color: #e0ebf6;
}
/* general styles for hyperlink */
a
{
	color: #03F;
	text-decoration: none;
	cursor :pointer;
}
a:hover
{
	color: #06F;
}
hr
{
	height: 1px;
	border: 0;
	color: #bbb;
	background-color: #bbb;
	width: 100%;	
}
/* logo text containing name of project */
h1
{
	margin: 0px;
	padding: 5px;
	font-size: 24px;
	background-color: #f3cece;
	text-align: center;
	color: #000;
	border-top-left-radius:5px;
	border-top-right-radius:5px;
	-moz-border-radius-topleft:5px;
	-moz-border-radius-topright:5px;
}
/* the div container for the links */
#headerlinks
{
	text-align:center;
	margin-bottom:10px;
	padding:5px;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	border-left-style:none;
	border-right-style:none;
	font-size:12px;
	background-color:#e0ebf6;
	font-weight:bold;
}
/* version text within the logo */
h1 #version
{
	color: #000000;
	font-size: 16px;
}
/* logo text within logo */
h1 #logo
{
	color:#000;
}
/* general header for various views */
h2
{
	margin:0px;
	padding:0px;
	font-size:14px;
	margin-bottom:20px;
}
/* input buttons and areas for entering text */
input, select, textarea
{
	font-family:Arial, Helvetica, sans-serif;
	background-color:#eaeaea;
	color:#03F;
	border-color:#03F;
	border-style:solid;
	border-width:1px;
	margin:5px;
	border-radius:5px;
	-moz-border-radius:5px;
	padding:3px;
}
/* just input buttons */
input.btn
{
	cursor:pointer;	
}
input.btn:hover
{
	background-color:#ccc;
}
/* general styles for hyperlink */
fieldset
{
	padding:15px;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	border-radius:5px;
	-moz-border-radius:5px;
	background-color:#f9f9f9;
}
/* outer div that holds everything */
#container
{
	padding:10px;
}
/* div of left box with log, list of databases, etc. */
#leftNav
{
	float:left;
	min-width:250px;
	padding:0px;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	background-color:#FFF;
	padding-bottom:15px;
	border-radius:5px;
	-moz-border-radius:5px;
}
/* div holding the content to the right of the leftNav */
#content
{
	overflow:hidden;
	padding-left:10px;
}
/* div holding the login fields */
#loginBox
{
	width:500px;
	margin-left:auto;
	margin-right:auto;
	margin-top:50px;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	background-color:#FFF;
	border-radius:5px;
	-moz-border-radius:5px;
}
/* div under tabs with tab-specific content */
#main
{
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	padding:15px;
	overflow:auto;
	background-color:#FFF;
	border-bottom-left-radius:5px;
	border-bottom-right-radius:5px;
	border-top-right-radius:5px;
	-moz-border-radius-bottomleft:5px;
	-moz-border-radius-bottomright:5px;
	-moz-border-radius-topright:5px;
}
/* odd-numbered table rows */
.td1
{
	background-color:#f9e3e3;
	text-align:right;
	font-size:12px;
	padding-left:10px;
	padding-right:10px;
}
/* even-numbered table rows */
.td2
{
	background-color:#f3cece;
	text-align:right;
	font-size:12px;
	padding-left:10px;
	padding-right:10px;
}
/* table column headers */
.tdheader
{
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	font-weight:bold;
	font-size:12px;
	padding-left:10px;
	padding-right:10px;
	background-color:#e0ebf6;
	border-radius:5px;
	-moz-border-radius:5px;
}
/* div holding the confirmation text of certain actions */
.confirm
{
	border-color:#03F;
	border-width:1px;
	border-style:dashed;
	padding:15px;
	background-color:#e0ebf6;
}
/* tab navigation for each table */
.tab
{
	display:block;
	padding:5px;
	padding-right:8px;
	padding-left:8px;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	margin-right:5px;
	float:left;
	border-bottom-style:none;
	position:relative;
	top:1px;
	padding-bottom:4px;
	background-color:#eaeaea;
	border-top-left-radius:5px;
	border-top-right-radius:5px;
	-moz-border-radius-topleft:5px;
	-moz-border-radius-topright:5px;
}
/* pressed state of tab */
.tab_pressed
{
	display:block;
	padding:5px;
	padding-right:8px;
	padding-left:8px;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	margin-right:5px;
	float:left;
	border-bottom-style:none;
	position:relative;
	top:1px;
	background-color:#FFF;
	cursor:default;
	border-top-left-radius:5px;
	border-top-right-radius:5px;
	-moz-border-radius-topleft:5px;
	-moz-border-radius-topright:5px;
}
/* help section */
.helpq
{
	font-size:11px;
	font-weight:normal;	
}
#help_container
{
	padding:0px;
	font-size:12px;
	margin-left:auto;
	margin-right:auto;
	background-color:#ffffff;
}
.help_outer
{
	background-color:#FFF;
	padding:0px;
	height:300px;
	overflow:hidden;
	position:relative;
}
.help_list
{
	padding:10px;
	height:auto;	
}

.headd
{
	font-size:14px;
	font-weight:bold;	
	display:block;
	padding:10px;
	background-color:#e0ebf6;
	border-color:#03F;
	border-width:1px;
	border-style:solid;
	border-left-style:none;
	border-right-style:none;
}
.help_inner
{
	padding:10px;	
}
.help_top
{
	display:block;
	position:absolute;
	right:10px;
	bottom:10px;	
}
</style>
<!-- end the customizable stylesheet/theme -->
<!-- JavaScript Support -->
<script type="text/javascript">
/* <![CDATA[ */
//initiated autoincrement checkboxes
function initAutoincrement()
{
	var i=0;
	while(document.getElementById('i'+i+'_autoincrement')!=undefined)
	{
		document.getElementById('i'+i+'_autoincrement').disabled = true;
		i++;
	}
}
//makes sure autoincrement can only be selected when integer type is selected
function toggleAutoincrement(i)
{
	var type = document.getElementById('i'+i+'_type');
	var primarykey = document.getElementById('i'+i+'_primarykey');
	var autoincrement = document.getElementById('i'+i+'_autoincrement');
	if(type.value=='INTEGER' && primarykey.checked)
		autoincrement.disabled = false;
	else
	{
		autoincrement.disabled = true;
		autoincrement.checked = false;
	}
}
function toggleNull(i)
{
	var pk = document.getElementById('i'+i+'_primarykey');
	var notnull = document.getElementById('i'+i+'_notnull');
	if(pk.checked)
	{
		notnull.disabled = true;
		notnull.checked = true;
	}
	else
	{
		notnull.disabled = false;
	}
}
//finds and checks all checkboxes for all rows on the Browse or Structure tab for a table
function checkAll(field)
{
	var i=0;
	while(document.getElementById('check_'+i)!=undefined)
	{
		document.getElementById('check_'+i).checked = true;
		i++;
	}
}
//finds and unchecks all checkboxes for all rows on the Browse or Structure tab for a table
function uncheckAll(field)
{
	var i=0;
	while(document.getElementById('check_'+i)!=undefined)
	{
		document.getElementById('check_'+i).checked = false;
		i++;
	}
}
//unchecks the ignore checkbox if user has typed something into one of the fields for adding new rows
function changeIgnore(area, e, u)
{
	if(area.value!="")
	{
		if(document.getElementById(e)!=undefined)
			document.getElementById(e).checked = false;
		if(document.getElementById(u)!=undefined)
			document.getElementById(u).checked = false;
	}
}
//moves fields from select menu into query textarea for SQL tab
function moveFields()
{
	var fields = document.getElementById("fieldcontainer");
	var selected = new Array();
	for(var i=0; i<fields.options.length; i++)
		if(fields.options[i].selected)
			selected.push(fields.options[i].value);
	for(var i=0; i<selected.length; i++)
		insertAtCaret("queryval", '"'+selected[i].replace(/"/g,'""')+'"');
}
//helper function for moveFields
function insertAtCaret(areaId,text)
{
	var txtarea = document.getElementById(areaId);
	var scrollPos = txtarea.scrollTop;
	var strPos = 0;
	var br = ((txtarea.selectionStart || txtarea.selectionStart == '0') ? "ff" : (document.selection ? "ie" : false ));
	if(br=="ie")
	{
		txtarea.focus();
		var range = document.selection.createRange();
		range.moveStart ('character', -txtarea.value.length);
		strPos = range.text.length;
	}
	else if(br=="ff")
		strPos = txtarea.selectionStart;

	var front = (txtarea.value).substring(0,strPos);
	var back = (txtarea.value).substring(strPos,txtarea.value.length);
	txtarea.value=front+text+back;
	strPos = strPos + text.length;
	if(br=="ie")
	{
		txtarea.focus();
		var range = document.selection.createRange();
		range.moveStart ('character', -txtarea.value.length);
		range.moveStart ('character', strPos);
		range.moveEnd ('character', 0);
		range.select();
	}
	else if(br=="ff")
	{
		txtarea.selectionStart = strPos;
		txtarea.selectionEnd = strPos;
		txtarea.focus();
	}
	txtarea.scrollTop = scrollPos;
}

function notNull(checker)
{
	document.getElementById(checker).checked = false;
}

function disableText(checker, textie)
{
	if(checker.checked)
	{
		document.getElementById(textie).value = "";
		document.getElementById(textie).disabled = true;	
	}
	else
	{
		document.getElementById(textie).disabled = false;	
	}
}

function toggleExports(val)
{
	document.getElementById("exportoptions_sql").style.display = "none";	
	document.getElementById("exportoptions_csv").style.display = "none";	
	
	document.getElementById("exportoptions_"+val).style.display = "block";	
}

function toggleImports(val)
{
	document.getElementById("importoptions_sql").style.display = "none";	
	document.getElementById("importoptions_csv").style.display = "none";	
	
	document.getElementById("importoptions_"+val).style.display = "block";	
}

function openHelp(section)
{
	PopupCenter('test_db.php?help=1#'+section, "Help Section");	
}
var helpsec = false;
function PopupCenter(pageURL, title)
{
	helpsec = window.open(pageURL, title, "toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=0,width=400,height=300");
} 
/* ]]> */ 
</script>
</head>
<body>
<div id='loginBox'><h1><span id='logo'>phpLiteAdmin</span> <span id='version'>v1.9.3</span></h1><div style='padding:15px; text-align:center;'><form action='test_db.php' method='post'>Password: <input type='password' name='password'/><br/><input type='checkbox' name='remember' value='yes' checked='checked'/> Remember me<br/><br/><input type='submit' value='Log In' name='login' class='btn'/><input type='hidden' name='proc_login' value='true' /></form></div></div><br/><div style='text-align:center;'><span style='font-size:11px;'>Powered by <a href='http://phpliteadmin.googlecode.com' target='_blank' style='font-size:11px;'>phpLiteAdmin</a> | Page generated in 0.0004 seconds.</span></div></body></html>