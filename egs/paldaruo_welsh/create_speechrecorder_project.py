#!/usr/bin/env python
import sys, os, csv, path, utils, shutil, codecs
import xml.etree.cElementTree as ET
import xml.dom.minidom as Pretty

projectconfig_template = """
<ProjectConfiguration version="3.4.0">
  <name>@@NAME@@</name>
  <recordingMixerName providerId="java:class:ips.audio.pulse.PulseMixerProvider">Built-in Audio Analog Stereo</recordingMixerName>
  <RecordingConfiguration>
    <url>@@AUDIO_URL@@</url>
    <Format>
      <channels>1</channels>
      <frameSize>2</frameSize>
      <sampleRate>48000.0</sampleRate>
    </Format>
    <captureScope>SESSION</captureScope>
  </RecordingConfiguration>
  <PromptConfiguration>
    <promptsUrl>@@PROMPTS_URL@@</promptsUrl>
    <StartStopSignal classname="ipsk.apps.speechrecorder.monitor.plugins.SimplePedestrianLights"/>
    <InstructionsFont>
      <family>SansSerif</family>
    </InstructionsFont>
    <PromptFont>
      <family>SansSerif</family>
    </PromptFont>
    <DescriptionFont>
      <family>SansSerif</family>
    </DescriptionFont>
    <ItemcodeGeneratorConfiguration>
      <prefix>demo_</prefix>
      <fixedDecimalPlaces>3</fixedDecimalPlaces>
    </ItemcodeGeneratorConfiguration>
    <PromptBeep>
      <beepGainRatio>1.0</beepGainRatio>
    </PromptBeep>
  </PromptConfiguration>
  <Speakers>
    <speakersUrl>@@SPEAKERS_URL@@</speakersUrl>
  </Speakers>
</ProjectConfiguration>
"""

def make_scriptfile(projectname, lang, source, destination):

	script = ET.Element("script")
	script.set("id",projectname + " script")

	recordingscript = ET.SubElement(script, "recordingscript")
	section = ET.SubElement(recordingscript,"section")

	prompts=utils.get_prompts(source)
	for key, value in prompts.iteritems():
		recording=ET.SubElement(section,"recording")
		recording.set("itemcode",key)
		recprompt=ET.SubElement(recording,"recprompt")
		mediaitem=ET.SubElement(recprompt,"mediaitem")
		mediaitem.set("languageISO639code",lang)	
		mediaitem.text=value
	
	promptsxmlstring = '<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE script SYSTEM "SpeechRecPrompts_2.dtd">'
	promptsxmlstring += ET.tostring(script)
	 
	prettyxml=Pretty.parseString(promptsxmlstring).toprettyxml(indent="   ")
	with codecs.open(destination,'w','utf-8') as out:
		out.write('')
		out.write(prettyxml)

def make_speakersfile(source, destination):

	speakers = ET.Element("speakers")

	metadata_file=csv.DictReader(open(source))
	for row in metadata_file:
		uid=row['uid']
		gender_cy=row['rhyw']
		if gender_cy=='benyw':
			gender='FEMALE'
		else:
			gender='MALE'
		speaker=ET.SubElement(speakers,"speakers")
		personId=ET.SubElement(speaker,"personId")
		personId.text=uid
		sex=ET.SubElement(speaker,"sex")
		sex.text=gender
		
	prettyxml=Pretty.parseString(ET.tostring(speakers)).toprettyxml(indent="   ")
        with codecs.open(destination,'w','utf-8') as out:
                out.write(prettyxml)

def make_projectfile(name, audio_url, prompts_url, speakers_url, destination):
	project=projectconfig_template.replace('\n','').replace('\r','')
	project=project.replace("@@NAME@@",name)
	project=project.replace("@@AUDIO_URL@@",audio_url)
	project=project.replace("@@PROMPTS_URL@@",prompts_url)
	project=project.replace("@@SPEAKERS_URL@@",speakers_url)

	prettyxml=Pretty.parseString(project).toprettyxml(indent="   ")
	with codecs.open(destination,'w','utf-8') as out:
		out.write(prettyxml)	

def create_speechrecorder_project(speechrecorder_project_home):
	if os.path.isdir(speechrecorder_project_home):
		shutil.rmtree(speechrecorder_project_home)

	os.makedirs(speechrecorder_project_home)
	shutil.copy('SpeechRecPrompts_2.dtd',speechrecorder_project_home)	
	
if __name__ == '__main__':
	try:
		source_dir = str(sys.argv[1])
		project_name = str(sys.argv[2])
		speechrecorder_projects_home = str(sys.argv[3])

		if not source_dir: raise 
		if not project_name: raise 
		if not speechrecorder_projects_home: raise
	except:
		print >> sys.stderr, "Usage %s <source_dir> <project_name> <speechrecorder_projects_home>" % sys.argv[0]
		sys.exit(0)

	print 'Creating SpeechRecorder project %s from files in %s in directory %s\n' % (project_name, source_dir, speechrecorder_projects_home)

	speechrecorder_project_home = os.path.join(speechrecorder_projects_home, project_name)

	audio_files_url = './' # relative to the project.prj file
	script_file_url = project_name + '_script.xml'
	speaker_file_url = project_name + '_speakers.xml'
	project_file_url = project_name + '_project.prj'
	lang = 'fi' # SpechRecorder doesn't include/support 'cy' Welsh

	create_speechrecorder_project(speechrecorder_project_home)

	make_projectfile(project_name, audio_files_url, script_file_url, speaker_file_url, os.path.join(speechrecorder_project_home, project_file_url))
	make_speakersfile(os.path.join(source_dir,'metadata.csv'), os.path.join(speechrecorder_project_home, speaker_file_url))
	make_scriptfile(project_name, lang, os.path.join(source_dir,'samples.txt'), os.path.join(speechrecorder_project_home, script_file_url))
 			
