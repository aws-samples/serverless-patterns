// ---------------------------------------------------------------------------
// <copyright file="Filter.cs" company="BP p.l.c.">
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

public class Filter
{
    public string Name { get; set; }
    public string[] Values { get; set; }
}