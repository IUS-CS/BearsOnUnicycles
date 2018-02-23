# Super Ultra Melees of History (SUMOH)

### Software Architecture Document
Version 0.1 (Draft)

## Revision History

| Date    | Version   | Description   | Author   |
|:-------:|:---------:|:-------------:|:--------:|
| 2/22/18 | 0.1       | First Draft   | Ben Heil | 

## Table of Contents

1. Introduction
    
    1. Purpose
    
2. Overview
    
    1. Key Terms

    2. Representation
    
    3. Framework

3. Architectural Goals

    1. Standards
       
    2. Constraints
    
    
## Introduction

**Purpose**


This document is designed to explain the software design of SUMOH
and its architecture. It will give an overview of the various systems
that SUMOH utilizes and define features that are novel to SUMOH. 

## Overview

**Key Terms**

This section defines some terminology that is useful when speaking
about video game design and SUMOH

- *Animation* - A collection of images that are displayed in an order to 
express movement
- *Animator* - A system that displays images in a certain order to 
form an animation. The system is a finite state machine that is defined by the
core logic
- *Collider* - A theoretical area where a game object exists and can
be interacted with by other game objects or the mechanics
- *Core Logic* - The background maths that is being done to control
the state of the game, including animations, mechanics, input, etc.
- *Game Loop* - The main procedure of the game, where all higher level
systems are called from
- *Game Object* - A theoretical representation of an object in the game.
All interactive elements in the game stem from this concept.
- *High Level Systems* - Broad systems in the architecture that govern many
small functions and utilities. These are the Animator, Mechanics, Core Logic, Input and Ouput.
- *Input* - The keyboard/joystick events that come from the user
- *Mechanics* - A System that dictates the possible outcomes in the game via a set of clearly defined rules.
It is analogous to the way that Physics dictate the possible outcomes in the 
real world. Note that the system does not define each individual outcome,
it only defines what can happen from event to event.
- *Output* - The Graphical User Interface (GUI) for the game. Here, the screen with
two fighters on it along with some other information about the state of the game
- *Pygame* - An open-source library for Python 2 and 3 that includes useful
code for video game implementation
- *Rendering* - Drawing elements on a screen with pixel math
- *Sprite Sheet* - An array of images that are equal in pixel area
that are displayed frame-wise to form an animation
- *Finite State Machine* - A system that has a clearly defined set of
states that are mutually exclusive and can be transitioned to only from 
certain other states by a clearly defined set of actions. A very important
concept that is essential to the Animation, Core Logic and I/O 


**Representation**

This section describes the three ways in which we will talk about SUMOH.


The first will be the user-facing or Front-End view. A view of the software
that is Abstracted from every system except the input and output. This view
is helpful when making design decisions that will impact user experience.


The Second will be the system-facing or Back-End view. This view examines
the interactions between high level systems in the code and the results of 
those interactions. This view is essential for understanding the design and implementation
of large-scale features in the game.

The final view will be the code-facing or low-level view. This view is at the unit level
and examines the way in which individual code elements perform their tasks and their input and
output. This view is essential for testing and optimization.

**Framework**

This section explains the framework that SUMOH is modeled after.

## Architectural Goals

**Standards**

This sections describes the requirements that SUMOH must satisfy to be considered viable
software

**Restraints**

This section describes the limitations that the developers of SUMOH are bound by 


    
    


