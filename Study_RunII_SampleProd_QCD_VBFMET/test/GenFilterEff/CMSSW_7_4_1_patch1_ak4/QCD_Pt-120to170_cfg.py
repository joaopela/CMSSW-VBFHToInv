# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ThirteenTeV/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8_cff.py --fileout file:QCD_Pt-120to170_step1.root --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM --pileup 2015_25ns_Startup_PoissonOOTPU --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions MCRUN2_74_V9 --beamspot NominalCollision2015 --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@frozen25ns --magField 38T_PostLS1 --python_filename QCD_Pt-120to170_step1_CMSSW_7_4_1_patch1_cfg.py --no_exec -n 100
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2015_25ns_Startup_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_25ns14e33_v1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

###############################################################
# START: Extra block for job making
###############################################################
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

# Input source
process.source = cms.Source("EmptySource",
  firstRun            =cms.untracked.uint32(1),
  firstLuminosityBlock=cms.untracked.uint32(JOBNUMBER)
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
  generator = cms.PSet(              # 900000000
    initialSeed = cms.untracked.uint32(JOBNUMBER),
    engineName = cms.untracked.string('HepJamesRandom')
  )
)
###############################################################
# END: Extra block for job making
###############################################################

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('QCD pthat 120to170 GeV, 13 TeV, TuneCUETP8M1'),
    name = cms.untracked.string('\\$Source$'),
    version = cms.untracked.string('\\$Revision$')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:QCD_Pt-120to170_step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/0028ABCB-74B0-E411-B596-0025904C4F50.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/007FD3D8-74B0-E411-AC02-782BCB67826E.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/00AAE11D-74B0-E411-BCF8-DF448471F33D.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/00BC66B7-6CAF-E411-86B6-20CF3056171F.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/00C59C87-75B0-E411-918F-63BFB108B170.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/02052468-72AF-E411-9F90-002590D9D990.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/022D9B0E-6EAF-E411-90AA-0022195E66A7.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/027B2D2C-74B0-E411-8DF1-001E682F8C7C.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/02B9B6A5-74B0-E411-A287-002590491B22.root', '/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/00000/02C48802-6EAF-E411-96A0-001E67248688.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring('HardQCD:all = on', 
            'PhaseSpace:pTHatMin = 120  ', 
            'PhaseSpace:pTHatMax = 170  '),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(471100.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

###############################################################
# START: Output control and sequence definition
###############################################################
# Generator level event filter definition
from CMSSW_VBFHToInv.Study_RunII_SampleProd_QCD_VBFMET.GenFilterAnalyzer_cfi import *
process.genFilterAnalyzer                           = genFilterAnalyzer
process.genFilterAnalyzer.outFile                   = cms.untracked.string('GenFilterAnalyzer_QCD_Pt-120to170_'+str(JOBNUMBER)+'.root')
process.genFilterAnalyzer.inputTag_GenJetCollection = cms.untracked.InputTag('ak4GenJetsNoNu')

# Path and EndPath definitions
#process.generation_step = cms.Path(process.pgen)
process.generation_step = cms.Path(
  process.generator*
  process.genParticles*
  process.genParticlesForJetsNoNu*
  process.ak4GenJetsNoNu*
  process.genFilterAnalyzer
)
process.simulation_step       = cms.Path(process.psim)
process.digitisation_step     = cms.Path(process.pdigi)
process.L1simulation_step     = cms.Path(process.SimL1Emulator)
process.digi2raw_step         = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step           = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step     = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step)
###############################################################
# END: Output control and sequence definition
###############################################################

# Path and EndPath definitions
#process.generation_step = cms.Path(process.pgen)
#process.simulation_step = cms.Path(process.psim)
#process.digitisation_step = cms.Path(process.pdigi)
#process.L1simulation_step = cms.Path(process.SimL1Emulator)
#process.digi2raw_step = cms.Path(process.DigiToRaw)
#process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
#process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
#
## Schedule definition
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
#process.schedule.extend(process.HLTSchedule)
#process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
## filter all path with the production filter sequence
#for path in process.paths:
#       getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions
