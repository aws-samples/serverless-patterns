// ---------------------------------------------------------------------------
// <copyright file="Settings.cs" company="BP p.l.c.">
// ---------------------------------------------------------------------------
// Copyright 2023 BP p.l.c. All Rights Reserved.
// Also protected by the Digital Millennium Copyright Act (DMCA) and
// afforded all remedies allowed under 17 U.S.C. § 1203.
// Proprietary and Confidential information of BP p.l.c.
// Disclosure, Use, or Reproduction without the written authorization
// of BP p.l.c. is prohibited.
// ---------------------------------------------------------------------------
// Author: Damodaran, Vedanayagan
// ---------------------------------------------------------------------------
// </copyright>
// ---------------------------------------------------------------------------

namespace Cdk.Models;

using System.Collections.Generic;

public class Settings
{
    public SnsTopic SnsTopic { get; set; }
    public IList<SqsQueue> SqsQueues { get; set; }
}